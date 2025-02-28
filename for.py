# Total jumping jacks required
total_jumping_jacks = 100
jumping_jacks_done = 0
set_size = 10

while jumping_jacks_done < total_jumping_jacks:
    jumping_jacks_done += set_size
    print(f"You have completed {jumping_jacks_done} jumping jacks.")

    if jumping_jacks_done >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {jumping_jacks_done} jumping jacks.")
            break
    remaining = total_jumping_jacks - jumping_jacks_done
    print(f"{remaining} jumping jacks remaining.\n")
