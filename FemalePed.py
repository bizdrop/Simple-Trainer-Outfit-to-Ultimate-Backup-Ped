def convert_to_ub_ped_female():
    print("Enter the values from Simple Trainer (enter -1 if unused):")

    head = int(input("Hat (prop_hats): "))
    upper = int(input("Upper (comp_shirt): "))
    lower = int(input("Lower (comp_pants): "))
    lower_texture = int(input("Lower Texture (tex_pants): "))
    hands = int(input("Hands (comp_hands): "))
    shoes = int(input("Shoes (comp_shoes): "))
    teeth = int(input("Teeth (comp_eyes): "))
    accessory = int(input("Accessory (comp_accessories): "))
    accessory_tex = int(input("Accessory Texture (tex_accessories): "))
    badges = int(input("Badges (comp_decals): "))
    shirt_overlay = int(input("Shirt Overlay (comp_shirtoverlay): "))
    shirt_overlay_tex = int(input("Shirt Overlay Texture (tex_shirtoverlay): "))

    chance = 2
    model = "MP_F_FREEMODE_01"
    tasks = 1
    tex_decals = 1
    tex_hands = 1

    attributes = [
        f'chance="{chance}"',
        f'prop_hats="{head}"' if head != -1 else "",
        f'comp_shirtoverlay="{shirt_overlay}" tex_shirtoverlay="{shirt_overlay_tex}"',
        f'comp_shirt="{upper}"',
        f'comp_decals="{badges}" tex_decals="{tex_decals}"',
        f'comp_accessories="{accessory}" tex_accessories="{accessory_tex}"',
        f'comp_pants="{lower}" tex_pants="{lower_texture}"',
        f'comp_shoes="{shoes}"',
        f'comp_eyes="{teeth}"',
        f'comp_tasks="{tasks}"',
        f'comp_hands="{hands}" tex_hands="{tex_hands}"'
    ]

    attributes = [attr for attr in attributes if attr]

    ped_config = f"<Ped {' '.join(attributes)}>{model}</Ped>"
    print("\nUltimate Backup Female Ped XML:\n")
    print(ped_config)


if __name__ == "__main__":
    convert_to_ub_ped_female()
