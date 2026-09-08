let rec factorial (n : int) : int =
    let rec factorial' (accum: int) (n : int) =
      if n = 0 then accum else factorial' (accum * n) (n-1)
    in
    factorial' 1 n

let () = print_endline (string_of_int (factorial 4))
