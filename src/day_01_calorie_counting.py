def most_calories_of_single_elf(raw_calories: list[str]) -> int:
    most_calories = 0
    current_calories = 0
    for food in raw_calories:
        if not food:
            current_calories = 0
            continue
        current_calories += int(food)
        if current_calories > most_calories:
            most_calories = current_calories
    return most_calories
