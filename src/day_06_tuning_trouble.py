def characters_before_start_marker(datastream_buffer: str) -> 0:
    for i in range(3, len(datastream_buffer) + 1):
        letter = datastream_buffer[i]
        if len({datastream_buffer[i - 1], datastream_buffer[i - 2], datastream_buffer[i - 3], letter}) == 4:
            return i + 1
    return 0
