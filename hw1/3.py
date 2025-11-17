compat = {
    "Aries": ["Leo", "Sagittarius"],
    "Taurus": ["Virgo", "Capricorn"],
    "Gemini": ["Libra", "Aquarius"],
    "Cancer": ["Scorpio", "Pisces"],
    "Leo": ["Aries", "Sagittarius"],
    "Virgo": ["Taurus", "Capricorn"],
    "Libra": ["Gemini", "Aquarius"],
    "Scorpio": ["Cancer", "Pisces"],
    "Sagittarius": ["Aries", "Leo"],
    "Capricorn": ["Taurus", "Virgo"],
    "Aquarius": ["Gemini", "Libra"],
    "Pisces": ["Cancer", "Scorpio"]
}

z1 = input("Your Zodiac: ").capitalize()
z2 = input("Partner's Zodiac: ").capitalize()

if z1 in compat and z2 in compat[z1]:
    print("Good Compatibility!")
else:
    print("Average or Low Compatibility.")
