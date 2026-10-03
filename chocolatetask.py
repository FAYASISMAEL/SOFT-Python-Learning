chocolates = {
	"kitkat": 10,
	"dairymilk": 100,
}

chocolate = input("Choose a chocolate (KitKat or DairyMilk): ").strip().lower()

if chocolate not in chocolates:
	print("Invalid chocolate choice.")
else:
	guess = int(input("Guess the price in rupees: "))
	if guess == chocolates[chocolate]:
		print(f"Correct! You get the {chocolate.title()} chocolate.")
	else:
		print("Wrong guess. Better luck next time!")
