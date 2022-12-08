def characters_before_start_marker(datastream_buffer: str, marker_size: int) -> 0:
    for i in range(3, len(datastream_buffer) + 1):
        if len(set(datastream_buffer[i - (marker_size - 1):i + 1])) == marker_size:
            return i + 1
    return 0
