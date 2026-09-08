let rec factorial (n : int) : int =
    let rec factorial' (accum: int) (n : int) =
      if n = 0 then accum else factorial' (accum * n) (n-1)
    in
    factorial' 1 n

let () = print_endline ("factorial 10 = " ^ string_of_int (factorial 10))

let rec fib n =
    if n = 0 then 0 else
    if n = 1 then 1 else
        fib (n-1) + fib (n-2)

(*
   a is the previous value
   b is the next value
*)
let rec fib' a b n =
    if n = 0 then a else
        fib' b (a+b) (n-1)

let () = print_endline ("fib 0 1 5 = " ^ string_of_int (fib' 0 1 5))

(* ********* TYPES ********* *)

type name = string
let my_name : name = "Max"

type height_cm = int
type height_in = int

let my_height : height_cm = 180

type person = name * height_cm

let me : person = (my_name, my_height)

let is_tall (p : person) : bool = snd p > 190

let is_tall ( (name, height) : person ) : bool = height > 190
