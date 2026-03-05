n = int(input())
hi = []
for _ in range(n):
    lol = input()
    hi.append(lol)
    
if "keys" not in hi:
    print("keys")
if "phone" not in hi:
    print("phone")
if "wallet" not in hi:
    print("wallet")
if "keys" in hi and "phone" in hi and "wallet" in hi:
    print("ready")