split_at_n([], _, [], [], []).
split_at_n([H|T], N, [H|Left], Middle, Right) :-
    H < N,
    split_at_n(T, N, Left, Middle, Right).

split_at_n([H|T], N, Left, [H|Middle], Right) :-
    H == N,
    split_at_n(T, N, Left, Middle, Right).

split_at_n([H|T], N, Left, Middle, [H|Right]) :-
    H > N,
    split_at_n(T, N, Left, Middle, Right).

quick_sort([], []).
quick_sort([Pivot|List], Result) :-
    split_at_n(List, Pivot, Left, Middle, Right),
    quick_sort(Left, Left_),
    quick_sort(Right, Right_),
    append(Left_, [Pivot|Middle], Result_),
    append(Result_, Right_, Result).