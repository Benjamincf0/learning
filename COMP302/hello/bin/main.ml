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

let is_tall ( (name, height) : person ) : bool = height > 191


(* ENUMERATED TYPES *)
type hand = Rock | Paper | Scissors

let my_hand = Rock
let your_hand = Paper

let beats (h1 : hand) (h2 : hand) : bool =
    match h1 with
    | Rock -> h2 = Scissors
                (* In this case, h1 (i.e. Rock) beats h2 when h2 is Scissors. *)
    | Paper -> h2 = Rock
    | Scissors -> h2 = Paper ;;

    (* by returining a bool, we can't express all three possible outcomes.
       There's a third outcome: a draw. *)

type outcome = Win | Lose | Draw

let play h1 h2 : outcome =
    match h1 with
        | Rock -> 
            (match h2 with
            | Rock -> Draw
            | Paper -> Lose
            | Scissors -> Win)
        | Paper ->
            begin match h2 with
                | Rock -> Win
                | Paper -> Draw
                | Scissors -> Lose
            end
        | Scissors ->
            begin match h2 with
                | Rock -> Lose
                | Paper -> Win
                | Scissors -> Draw
            end

let play h1 h2 : outcome =
    if h1 = h2 then Draw
    else if beats h1 h2 then Win
    else Lose

let play h1 h2 : outcome =
    if h1 = h2 then Draw else
        match (h1, h2) with
        | (Rock, Paper) -> Lose
        | (Paper, Scissors) -> Lose
        | (Scissors, Rock) -> Lose
        | _ -> Win

let play h1 h2 : outcome =
    match (h1, h2) with
    | (me, you) when me = you -> Draw
    | (Rock, Paper) -> Lose
    | (Paper, Scissors) -> Lose
    | (Scissors, Rock) -> Lose
    | _ -> Win
