; move_mouse_read_file.ahk
MoveMouseFromFile() {
    ; Read the coordinates from the file
    coordinates := FileRead("coordinates.txt")
    if (coordinates = "") {
        MsgBox("Error: Could not read coordinates file.")
        return
    }

    ; Split the coordinates by comma
    coords := StrSplit(coordinates, ",")
    if (coords.Length >= 2) {  ; Use Length without parentheses
        x := coords[1]
        y := coords[2]
        MouseMove(x, y, 0) ; Moves mouse instantly to (x, y)
    } else {
        MsgBox("Error: Invalid coordinates format.")
    }
}

; Call the function
MoveMouseFromFile()
