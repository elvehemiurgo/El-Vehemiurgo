; ============================================================
;  vehemiurgo-captura.ahk — captura de takes desde VLC
;  Satélite LOCAL de El Vehemiurgo (kit: satelite-local/captura-vlc/)
;
;  Qué hace: con VLC reproduciendo un show de la mediateca, una
;  combinación de teclas pausa el video, lee QUÉ archivo está sonando
;  y EN QUÉ minuto, abre una ventanita para dictar el take, y lo
;  anota en el borrador del día con el formato que la sesión de
;  VEHEMIURGIA consume tal cual (/volcado).
;
;  Requiere: AutoHotkey v2 + interfaz web de VLC activada
;  (ver README.md de esta carpeta).
; ============================================================

#Requires AutoHotkey v2.0
#SingleInstance Force
Persistent

; ---------------- CONFIG (editar acá) ----------------
VLC_HOST         := "127.0.0.1"
VLC_PORT         := 8080
VLC_PASSWORD     := "vehemiurgo"          ; la misma que en VLC > Lua HTTP
BORRADOR_DIR     := "E:\VEHEWRES\borradores"
PAUSE_ON_CAPTURE := true                  ; pausa VLC mientras dictás
; ------------------------------------------------------

; ---------------- HOTKEYS ----------------
^!v:: CapturarTake()      ; Ctrl+Alt+V  → take completo (lucha / segmento)
^!m:: CapturarMarca()     ; Ctrl+Alt+M  → solo marca de tiempo + etiqueta corta
^!b:: AbrirBorrador()     ; Ctrl+Alt+B  → abre el borrador de hoy
; -----------------------------------------

TrayTip("Vehemiurgo captura VLC", "Ctrl+Alt+V take · Ctrl+Alt+M marca · Ctrl+Alt+B borrador", 1)

; ============================================================
;  VLC — interfaz HTTP
; ============================================================

VlcGet(query := "") {
    url := "http://" VLC_HOST ":" VLC_PORT "/requests/status.json" query
    try {
        req := ComObject("WinHttp.WinHttpRequest.5.1")
        req.Open("GET", url, false)
        req.SetRequestHeader("Authorization", "Basic " Base64(":" VLC_PASSWORD))
        req.SetCredentials("", VLC_PASSWORD, 0)
        req.Send()
        if (req.Status != 200)
            return ""
        return req.ResponseText
    } catch {
        return ""
    }
}

VlcCmd(cmd) {
    VlcGet("?command=" cmd)
}

; Devuelve un objeto {show, ts, state, fuente} o show="" si no hay nada.
Contexto() {
    info := {show: "", ts: "", state: "", fuente: ""}
    json := VlcGet()
    if (json != "") {
        fn := RegExMatch(json, '"filename":\s*"((?:[^"\\]|\\.)*)"', &m) ? JsonUnescape(m[1]) : ""
        if (fn = "")
            fn := RegExMatch(json, '"title":\s*"((?:[^"\\]|\\.)*)"', &m) ? JsonUnescape(m[1]) : ""
        t  := RegExMatch(json, '"time":\s*(\d+)', &m) ? Integer(m[1]) : -1
        st := RegExMatch(json, '"state":\s*"([a-z]+)"', &m) ? m[1] : ""
        if (fn != "") {
            info.show   := NombreShow(fn)
            info.ts     := (t >= 0) ? FmtTiempo(t) : "sin timestamp"
            info.state  := st
            info.fuente := "http"
            return info
        }
    }
    ; Fallback: sin interfaz web, leer el título de la ventana de VLC
    ; (da el archivo pero NO el minuto).
    if WinExist("ahk_exe vlc.exe") {
        titulo := WinGetTitle("ahk_exe vlc.exe")
        titulo := RegExReplace(titulo, "\s-\s(VLC media player|Reproductor multimedia VLC)$", "")
        if (titulo != "" && titulo != "VLC media player" && titulo != "Reproductor multimedia VLC") {
            info.show   := NombreShow(titulo)
            info.ts     := "sin timestamp"
            info.fuente := "titulo"
        }
    }
    return info
}

NombreShow(fn) {
    fn := RegExReplace(fn, "^.*[\\/]", "")              ; quitar ruta si viene
    fn := RegExReplace(fn, "\.[A-Za-z0-9]{2,4}$", "")   ; quitar extensión
    return Trim(fn)
}

FmtTiempo(t) {
    return Format("{:02}:{:02}:{:02}", t // 3600, (t // 60) mod 60, t mod 60)
}

JsonUnescape(s) {
    s := StrReplace(s, "\/", "/")
    s := StrReplace(s, '\"', '"')
    ; \uXXXX → carácter
    pos := 1
    while RegExMatch(s, "\\u([0-9A-Fa-f]{4})", &m, pos) {
        ch := Chr(Integer("0x" m[1]))
        s := SubStr(s, 1, m.Pos - 1) ch SubStr(s, m.Pos + m.Len)
        pos := m.Pos + StrLen(ch)
    }
    s := StrReplace(s, "\\", "\")
    return s
}

Base64(str) {
    n := StrPut(str, "UTF-8")            ; incluye el null final
    buf := Buffer(n)
    StrPut(str, buf, "UTF-8")
    bytes := n - 1
    len := 0
    DllCall("Crypt32\CryptBinaryToStringW", "Ptr", buf, "UInt", bytes, "UInt", 0x40000001, "Ptr", 0, "UInt*", &len)
    out := Buffer(len * 2)
    DllCall("Crypt32\CryptBinaryToStringW", "Ptr", buf, "UInt", bytes, "UInt", 0x40000001, "Ptr", out, "UInt*", &len)
    return StrGet(out, "UTF-16")
}

; ============================================================
;  Captura
; ============================================================

CapturarTake() {
    info := Contexto()
    if (info.show = "") {
        MsgBox("No encuentro nada sonando en VLC.`n`n¿Está abierto? ¿Está activada la interfaz web (ver README)?", "Vehemiurgo captura", "Icon!")
        return
    }
    pausado := false
    if (PAUSE_ON_CAPTURE && info.state = "playing") {
        VlcCmd("pl_forcepause")
        pausado := true
    }
    texto := Dialogo(info, "Take — Enter guarda · Ctrl+Enter salto de línea · Esc cancela", 10)
    if pausado
        VlcCmd("pl_forceresume")
    if (texto = "")
        return
    Escribir(info, texto)
}

CapturarMarca() {
    info := Contexto()
    if (info.show = "") {
        MsgBox("No encuentro nada sonando en VLC.", "Vehemiurgo captura", "Icon!")
        return
    }
    etiqueta := Dialogo(info, "Marca — etiqueta corta (ej. 'arranca el main event')", 2)
    if (etiqueta = "")
        return
    Escribir(info, "_(marca)_ " etiqueta)
}

Dialogo(info, titulo, filas) {
    resultado := ""
    g := Gui("+AlwaysOnTop +ToolWindow", "Vehemiurgo · " titulo)
    g.SetFont("s10", "Segoe UI")
    g.AddText("w640", "▶  " info.show "    ⏱  " info.ts (info.fuente = "titulo" ? "   (sin interfaz web: no hay minuto)" : ""))
    ed := g.AddEdit("w640 r" filas " Multi")
    btnOk := g.AddButton("Default w120", "Guardar")
    btnNo := g.AddButton("x+10 w120", "Cancelar")
    btnOk.OnEvent("Click", (*) => (resultado := Trim(ed.Value, " `t`r`n"), g.Destroy()))
    btnNo.OnEvent("Click", (*) => g.Destroy())
    g.OnEvent("Escape", (*) => g.Destroy())
    g.OnEvent("Close", (*) => g.Destroy())
    g.Show()
    ed.Focus()
    WinWaitClose("ahk_id " g.Hwnd)
    return resultado
}

Escribir(info, texto) {
    hoy := FormatTime(, "yyyy-MM-dd")
    path := BORRADOR_DIR "\" hoy "-borrador.md"
    if !DirExist(BORRADOR_DIR)
        DirCreate(BORRADOR_DIR)
    if !FileExist(path) {
        FileAppend("# Borrador de visionado — " hoy "`n`n"
                 . "> Capturado con vehemiurgo-captura.ahk desde VLC. Se pega TAL CUAL en la sesión de VEHEMIURGIA (/volcado): "
                 . "el encabezado `## YYYY MM DD Nombre del Show` fija fecha y show de cada ficha; el `[HH:MM:SS]` es la ubicación en el show.`n`n", path, "UTF-8")
    }
    if (UltimoShow(path) != info.show)
        FileAppend("## " info.show "`n`n", path, "UTF-8")
    texto := StrReplace(texto, "`r`n", " / ")
    texto := StrReplace(texto, "`n", " / ")
    FileAppend("- **[" info.ts "]** " texto "`n", path, "UTF-8")
    TrayTip(info.show " @ " info.ts, SubStr(texto, 1, 120), 1)
}

; Último encabezado "## ..." del borrador (para no repetir el show).
UltimoShow(path) {
    if !FileExist(path)
        return ""
    ultimo := ""
    Loop Read, path {
        if (SubStr(A_LoopReadLine, 1, 3) = "## ")
            ultimo := Trim(SubStr(A_LoopReadLine, 4))
    }
    return ultimo
}

AbrirBorrador() {
    path := BORRADOR_DIR "\" FormatTime(, "yyyy-MM-dd") "-borrador.md"
    if FileExist(path)
        Run(path)
    else
        MsgBox("Todavía no hay borrador hoy:`n" path, "Vehemiurgo captura", "Icon!")
}
