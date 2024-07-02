import math


def generate_factors(c):
    factors = set()  # Using a set to store factors to automatically remove duplicates
    for i in range(1, int(math.sqrt(c)) + 1):
        if c % i == 0:
            factors.add(i)
            factors.add(c // i)
    return factors


def generate_pythagorean_triples(c):
    # Set to store unique pairs (a, b) where a^2 + b^2 = c^2
    pairs = set()

    # Step 1: Generate factors of c
    factors = generate_factors(c)

    # Step 2: Iterate over all divisors of c
    for k in factors:
        s = c // k  # Compute s = c / k

        # Step 3: Iterate over possible values of n
        for n in range(1, math.isqrt(s // 2) + 1):
            m_square = s - n**2
            m = int(math.sqrt(m_square))  # Find m such that m^2 = s - n^2

            # If m is an integer (m^2 = s - n^2)
            if m**2 == m_square:
                a = k * (m**2 - n**2)  # Compute a
                b = k * (2 * m * n)  # Compute b
                # Add (a, b) to the set of pairs
                pairs.add(
                    (min(a, b), max(a, b))
                )  # Ensure a < b by sorting before adding

    return pairs


# Example usage:
c = int(input())
triples = generate_pythagorean_triples(c)
print(len(triples))
