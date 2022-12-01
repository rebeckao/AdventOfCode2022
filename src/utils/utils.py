def lines_from_file(file_name: str) -> list[str]:
    with open(f'../test_data/{file_name}') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]