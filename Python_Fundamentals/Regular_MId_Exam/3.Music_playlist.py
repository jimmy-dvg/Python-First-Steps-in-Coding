def main() -> None:
	playlist = input().split()
	commands_count = int(input())

	for _ in range(commands_count):
		command_parts = input().split(" * ")
		command = command_parts[0]

		if command == "Add Song":
			song = command_parts[1]
			if song not in playlist:
				playlist.append(song)
				print(f"{song} successfully added")

		elif command == "Delete Song":
			count = int(command_parts[1])
			if count <= len(playlist):
				deleted_songs = playlist[:count]
				del playlist[:count]
				print(f"{', '.join(deleted_songs)} deleted")

		elif command == "Shuffle Songs":
			first_index = int(command_parts[1])
			second_index = int(command_parts[2])

			if 0 <= first_index < len(playlist) and 0 <= second_index < len(playlist):
				playlist[first_index], playlist[second_index] = (
					playlist[second_index],
					playlist[first_index],
				)
				print(
					f"{playlist[first_index]} is swapped with {playlist[second_index]}"
				)

		elif command == "Insert":
			song = command_parts[1]
			index = int(command_parts[2])

			if 0 <= index < len(playlist):
				if song in playlist:
					print("Song is already in the playlist")
				else:
					playlist.insert(index, song)
					print(f"{song} successfully inserted")
			else:
				print("Index out of range")

		elif command == "Sort":
			playlist.sort(reverse=True)

		elif command == "Play":
			print("Songs to Play:")
			print("\n".join(playlist))


if __name__ == "__main__":
	main()
