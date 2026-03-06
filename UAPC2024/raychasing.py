import sys

def add_candidate(cands, name, num, den, x_num=None, y_num=None, den_common=None):
    # num/den is t; require den>0 and t>0
    if den < 0:
        num, den = -num, -den
    if num <= 0:
        return
    cands.append((name, num, den, x_num, y_num, den_common))

def in_range_scaled(val_num, den, lo, hi):
    # checks lo <= val_num/den <= hi using integer arithmetic
    return lo * den <= val_num <= hi * den

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    X1, X2, Y1, Y2 = map(int, data[:4])
    Xs, Ys, Xr, Yr = map(int, data[4:8])

    dx = Xr - Xs
    dy = Yr - Ys

    cands = []

    # Vertical sides: x = X1 (left), x = X2 (right)
    if dx != 0:
        # left
        num = X1 - Xs
        den = dx
        # y = Ys + t*dy = (Ys*den + num*dy)/den
        # Use common den = den (after sign normalization in add_candidate)
        # We'll store y_num and den_common to range-check after normalization ourselves:
        # easier: normalize here for checking
        d = den
        n = num
        if d < 0:
            n, d = -n, -d
        if n > 0:
            y_num = Ys * d + n * dy
            if in_range_scaled(y_num, d, Y1, Y2):
                add_candidate(cands, "left", num, den)

        # right
        num = X2 - Xs
        den = dx
        d = den
        n = num
        if d < 0:
            n, d = -n, -d
        if n > 0:
            y_num = Ys * d + n * dy
            if in_range_scaled(y_num, d, Y1, Y2):
                add_candidate(cands, "right", num, den)

    # Horizontal sides: y = Y1 (bottom), y = Y2 (top)
    if dy != 0:
        # bottom
        num = Y1 - Ys
        den = dy
        d = den
        n = num
        if d < 0:
            n, d = -n, -d
        if n > 0:
            x_num = Xs * d + n * dx
            if in_range_scaled(x_num, d, X1, X2):
                add_candidate(cands, "bottom", num, den)

        # top
        num = Y2 - Ys
        den = dy
        d = den
        n = num
        if d < 0:
            n, d = -n, -d
        if n > 0:
            x_num = Xs * d + n * dx
            if in_range_scaled(x_num, d, X1, X2):
                add_candidate(cands, "top", num, den)

    # Find minimum t among candidates
    # Compare (n1/d1) vs (n2/d2) by n1*d2 < n2*d1
    best = []
    best_n = best_d = None

    for name, n, d, *_ in cands:
        # normalize sign for comparison
        if d < 0:
            n, d = -n, -d
        if best_n is None:
            best_n, best_d = n, d
            best = [name]
        else:
            lhs = n * best_d
            rhs = best_n * d
            if lhs < rhs:
                best_n, best_d = n, d
                best = [name]
            elif lhs == rhs:
                best.append(name)

    # If tie includes both a vertical and horizontal side -> corner
    best_set = set(best)
    vertical = {"left", "right"}
    horizontal = {"bottom", "top"}

    if len(best_set) == 1:
        print(next(iter(best_set)))
        return

    v = list(best_set & vertical)
    h = list(best_set & horizontal)

    if v and h:
        vx = v[0]
        hy = h[0]
        if hy == "top" and vx == "left":
            print("top-left")
        elif hy == "top" and vx == "right":
            print("top-right")
        elif hy == "bottom" and vx == "left":
            print("bottom-left")
        else:
            print("bottom-right")
    else:
        # Degenerate tie on parallel sides shouldn't happen for a point strictly inside,
        # but just in case, prefer deterministic output.
        print(sorted(best_set)[0])

if __name__ == "__main__":
    main()