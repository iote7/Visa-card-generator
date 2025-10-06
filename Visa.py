import random
import time
import sys
import string
from typing import Tuple

def luhn_checksum(card_number: str) -> int:
    """Calculate Luhn checksum for card validation."""
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(digits_of(2 * d)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def generate_visa_number() -> str:
    """Generate a Luhn-valid Visa card number (16 digits)."""
    card = [4] + [random.randint(0, 9) for _ in range(14)]
    for check_digit in range(10):
        test_card = card + [check_digit]
        if luhn_checksum(''.join(map(str, test_card))) == 0:
            card.append(check_digit)
            return ''.join(map(str, card))
    card.append(random.randint(0, 9))
    return ''.join(map(str, card))

def random_name() -> str:
    """Generate a random uppercase name."""
    first = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5,8)))
    last = ''.join(random.choices(string.ascii_uppercase, k=random.randint(7,10)))
    return f"{first} {last}"

def random_expiry() -> str:
    """Generate a random expiry date in MM/YY format."""
    month = f"{random.randint(1,12):02d}"
    year = str(random.randint(25, 35))
    return f"{month}/{year}"

def random_cvv() -> str:
    """Generate a random 3-digit CVV."""
    return f"{random.randint(100,999)}"

def hacking_style_print(text: str, delay: float = 0.01):
    """Print with a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ascii_banner(text: str) -> None:
    """Print a simple ASCII banner."""
    banner = f"""
==================================================
   ███    ██ ██ ███████  █████   ██████   ██████  
   ████   ██ ██ ██      ██   ██ ██    ██ ██       
   ██ ██  ██ ██ █████   ███████ ██    ██ ██   ███ 
   ██  ██ ██ ██ ██      ██   ██ ██    ██ ██    ██ 
   ██   ████ ██ ███████ ██   ██  ██████   ██████  
==================================================
{text.center(48)}
==================================================
"""
    print(banner)

def generate_card_data() -> Tuple[str, str, str, str]:
    """Generate a set of card data."""
    return (
        generate_visa_number(),
        random_name(),
        random_expiry(),
        random_cvv()
    )

def main():
    ascii_banner("VISA CARD GENERATOR")
    hacking_style_print("Initializing sequence...", delay=0.04)
    time.sleep(1)
    for i in range(5):
        hacking_style_print(f"\n[+] Generating card #{i+1} ...", delay=0.02)
        visa, name, exp, cvv = generate_card_data()
        hacking_style_print(f"    [Card Number]  {visa}")
        hacking_style_print(f"    [Name]         {name}")
        hacking_style_print(f"    [Expiry]       {exp}")
        hacking_style_print(f"    [CVV]          {cvv}")
        hacking_style_print("-" * 50, delay=0.002)
        time.sleep(0.4)
    hacking_style_print("Sequence complete.", delay=0.03)

if __name__ == "__main__":
    main()
