import re
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation_value: int
    operation_type: str
    divisible_value: int
    target_true: int
    target_false: int
    inspections: 0

    def modify_worry(self, original_worry):
        if self.operation_type == "+":
            return original_worry + self.operation_value
        elif self.operation_type == "*":
            return original_worry * self.operation_value
        elif self.operation_type == "square":
            return original_worry * original_worry
        else:
            print(self)


def level_of_monkey_business(raw_lines: list[str]) -> int:
    monkeys = _parse_monkeys(raw_lines)
    for _ in range(0, 20):
        for monkey_number in range(0, len(monkeys)):
            monkey = monkeys[monkey_number]
            for item in monkey.items:
                worry = monkey.modify_worry(item)
                worry = int(worry / 3)
                if worry % monkey.divisible_value == 0:
                    target = monkey.target_true
                else:
                    target = monkey.target_false
                monkeys[target].items.append(worry)
                monkey.inspections += 1
            monkey.items = []
    inspections = [monkeys[m].inspections for m in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def _parse_monkeys(raw_lines: list[str]) -> dict[int, Monkey]:
    monkeys = dict()
    current_line = 0
    while current_line < len(raw_lines):
        monkey_number = int(re.search(r"Monkey (\d+):", raw_lines[current_line]).group(1))
        items = [int(x) for x in re.search(r"Starting items: (.*)", raw_lines[current_line + 1]).group(1).split(", ")]
        operation_type, raw_operation_value = re.search(r"Operation: new = old (.*) (.*)", raw_lines[current_line + 2]).groups()
        divisible_value = int(re.search(r"Test: divisible by (\d+)", raw_lines[current_line + 3]).group(1))
        target_true = int(re.search(r"If true: throw to monkey (\d+)", raw_lines[current_line + 4]).group(1))
        target_false = int(re.search(r"If false: throw to monkey (\d+)", raw_lines[current_line + 5]).group(1))
        if raw_operation_value == "old" and operation_type == "*":
            operation_value = 1
            operation_type = "square"
        else:
            operation_value = int(raw_operation_value)
        monkey = Monkey(items, operation_value, operation_type, divisible_value, target_true, target_false, 0)
        monkeys[monkey_number] = monkey
        current_line += 7
    return monkeys
