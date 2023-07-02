import PySimpleGUI as sg

class t:
 def __init__(self) -> None:
  self.Blood_Hunter =[
sg.Text("Blood-Hunter",s=(45,1),pad=(0,4),font=('Helvetica',20))

,sg.Text("Hit Points",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Hit Dice: 1d10 per blood hunter level",pad=(0,0),font=('Helvetica',10))

,sg.Text("Hit Points at 1st Level: 10 + your Constitution modifier",pad=(0,0),font=('Helvetica',10))

,sg.Text("Hit Points at Higher Levels: 1d10 (or 6) + your Constitution modifier per blood hunter level after 1st",pad=(0,0),font=('Helvetica',10))

,sg.Text("Proficiencies",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Armor: Light armor, medium armor, shields",pad=(0,0),font=('Helvetica',10))

,sg.Text("Weapons: Simple weapons, martial weapons",pad=(0,0),font=('Helvetica',10))

,sg.Text("Tools: Alchemist's supplies",pad=(0,0),font=('Helvetica',10))

,sg.Text("Saving Throws: Dexterity, Intelligence",pad=(0,0),font=('Helvetica',10))

,sg.Text("Skills: Choose three from Acrobatics, Arcana, Athletics, History, Insight, Investigation, Religion, and Survival",pad=(0,0),font=('Helvetica',10))

,sg.Text("Equipment",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("	- (a) a martial weapon or (b) two simple weapons",pad=(0,0),font=('Helvetica',10))

,sg.Text("	- (a) a light crossbow and 20 bolts or (b) hand crossbow and 20 bolts",pad=(0,0),font=('Helvetica',10))

,sg.Text("	- (a) studded leather armor or (b) scale mail armor",pad=(0,0),font=('Helvetica',10))

,sg.Text("	- an explorer's pack and alchemist's supplies",pad=(0,0),font=('Helvetica',10))

,sg.DropDown(['Club', 'Dagger', 'Greatclub', 'Handaxe', 'Javelin', 'Light hammer', 'Mace', 'Quarterstaff', 'Sickle', 'Spear', 'Crossbow, light', 'Dart', 'Shortbow', 'Sling'],s=(25,10),readonly=True,default_value='')

,sg.DropDown(['Club', 'Dagger', 'Greatclub', 'Handaxe', 'Javelin', 'Light hammer', 'Mace', 'Quarterstaff', 'Sickle', 'Spear', 'Crossbow, light', 'Dart', 'Shortbow', 'Sling'],s=(25,10),readonly=True,default_value='')

,sg.DropDown(['Studded leather','Scale mail'],s=(25,10),readonly=True,default_value='Studded leather')

,sg.Text("Level 1",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Hunter’s Bane",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("At 1st level, you have survived the Hunter’s Bane—a dangerous, long-guarded ritual that alters your life’s blood, forever binding you to the darkness and honing your senses against it. You have advantage on Wisdom (Survival) checks to track fey, fiends, or undead, as well as on Intelligence checks to recall information about such creatures.",s=(80,4),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("The Hunter’s Bane also empowers your body to control and shape hemocraft magic, using your own blood and life essence to fuel your abilities. Some of your features require your target to make a saving throw to resist the feature’s effects. The saving throw DC is calculated as follows:",s=(80,4),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("Hemocraft save DC = 8 + your proficiency bonus + your Hemocraft modifier (your choice between Intelligence and Wisdom)",pad=(0,0),font=('Helvetica',10))

,sg.Multiline("Also at 1st level, you gain the ability to channel—or sometimes sacrifice—a part of your vital essence to curse and manipulate creatures through hemocraft magic. You know one Blood Curse of your choice. You learn one additional blood curse of your choice at 6th, 10th, 14th, and 18th level. Each time you learn a new blood curse, you can also choose one of the blood curses you know and replace it with another blood curse.",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("Each time you use your Blood Maledict feature, you choose which curse to invoke from the curses you know. While invoking a blood curse, but before it affects the target, you can choose to amplify the curse by taking necrotic damage equal to one roll of your hemocraft die. This damage can’t be reduced in any way. An amplified curse gains an additional effect, noted in the curse’s description. Creatures that do not have blood are immune to blood curses unless you have amplified the curse.",s=(80,6),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("Once you use this feature, you must finish a short or long rest before you can use it again. You can use Blood Maledict twice between rests starting at 6th level, three times starting at 13th level, and four times starting at 17th level.",s=(80,3),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("Level 2",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Fighting Style",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("At 2nd level, you adopt a style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again.",s=(80,3),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("	- Archery. You gain a +2 bonus to attack rolls you make with ranged weapons.",pad=(0,0),font=('Helvetica',10))

,sg.Multiline("- Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",s=(80,2),pad=(60,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("- Great Weapon Fighting. When you roll a 1 or 2 on a non-rite damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property for you to gain this benefit.",s=(80,4),pad=(60,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("- Two-Weapon Fighting. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",s=(80,2),pad=(60,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.DropDown(['Archery','Dueling','Great Weapon Fighting','Two-Weapon Fighting'],s=(25,10),readonly=True,default_value='Archery')

,sg.Text("Crimson Rites",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("Also at 2nd level, you learn to invoke a rite of hemocraft that infuses your weapon strikes with elemental energy. As a bonus action, you can activate any rite you know on one weapon you’re holding. The effect of the rite lasts until you finish a short or long rest. When you activate a rite, you take necrotic damage equal to one roll of your hemocraft die. This damage can’t be reduced in any way.",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("While the rite is in effect, attacks you make with this weapon are magical, and deal extra damage equal to your hemocraft die of the type determined by the chosen rite. A weapon can hold only one active rite at a time. Other creatures can’t gain the benefit of your rite.",s=(80,3),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("You choose one rite from the crimson rites below when you first gain this feature. You learn an additional crimson rite at 7th level, and again at 14th level.",s=(80,2),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("Rite of the Flame. Your rite damage is fire damage.",pad=(0,0),font=('Helvetica',10))

,sg.Text("Rite of the Frozen. Your rite damage is cold damage.",pad=(0,0),font=('Helvetica',10))

,sg.Text("Rite of the Storm. Your rite damage is lightning damage.",pad=(0,0),font=('Helvetica',10))

,sg.Text("Rite of the Dead. Your rite damage is necrotic damage. (Prerequisite: 14th level)",pad=(0,0),font=('Helvetica',10))

,sg.Text("Rite of the Oracle. Your rite damage is psychic damage. (Prerequisite: 14th level)",pad=(0,0),font=('Helvetica',10))

,sg.Text("Rite of the Roar. Your rite damage is thunder damage. (Prerequisite: 14th level)",pad=(0,0),font=('Helvetica',10))

,sg.DropDown(['Flame', 'Frozen','Storm','Dead','Oracle','Roar'],s=(25,10),readonly=True,default_value='')

,sg.Text("Level 3",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Blood Hunter Order",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("At 3rd level, you commit to an order of blood hunters whose philosophy will guide you throughout your life. The order you choose grants you features at 3rd level, and again at 7th, 11th, 15th, and 18th level.",s=(80,3),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.DropDown(['Ghostslayer', 'Lycan','Mutant','Profane Soul'],s=(25,10),readonly=True,default_value='')

,sg.Text('Subclass Feature',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("And its rather lengthy description",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text('Level 4',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Ability Score Improvement',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.Text("Level 5",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Extra Attack",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Starting at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.",pad=(0,0),font=('Helvetica',10))

,sg.Text("Brand of Castigation",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Level 6",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("At 6th level, when you damage a creature with a weapon for which you have an active crimson rite, you can channel hemocraft magic to sear an arcane brand into that creature (no action required). You always know the direction to the branded creature as long as it’s on the same plane as you. Further, each time the branded creature deals damage to you or a creature you can see within 5 feet of you, the branded creature takes psychic damage equal to your Hemocraft modifier (minimum of 1).",s=(80,6),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("Your brand lasts until you dismiss it or until you use this feature to apply a brand to another creature. Your brand can be dispelled with Dispel Magic, and is treated as a spell with a level equal to half your blood hunter level (maximum 9th level).",s=(80,3),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("Once you use this feature, you can’t use it again until you finish a short or long rest.",pad=(0,0),font=('Helvetica',10))

,sg.Text("Level 7",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Subclass Feature',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("And its rather lengthy description",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text('Level 8',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Ability Score Improvement',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.Text("Level 9",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Grim Psychometry",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("When you reach 9th level, you gain a supernatural talent for discerning the secrets surrounding mysterious relics or places touched by evil. Whenever you make an Intelligence (History) check to recall information about the sinister or tragic history of an object you are touching or your current location, you have advantage on the check. At the DM’s discretion, a suitably high roll might cause your character to experience brief visions of the past connected to the object or location.",s=(80,6),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("Level 10",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Dark Augmentation",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("Starting at 10th level, the magic of hemocraft suffuses your body to permanently reinforce your resilience. Your speed increases by 5 feet, and you have a bonus to Strength, Dexterity, and Constitution saving throws equal to your Hemocraft modifier (minimum of +1).",s=(80,3),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("Level 11",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Subclass Feature',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("And its rather lengthy description",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text('Level 12',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Ability Score Improvement',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.Text("Level 13",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Brand of Tethering",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("Starting at 13th level, the psychic damage from your Brand of Castigation increases to twice your Hemocraft modifier (minimum of 2). Additionally, a branded creature can’t take the Dash action, and if it attempts to teleport or to leave its current plane by any means, it takes 4d6 psychic damage and must make a Wisdom saving throw. On a failure, the attempt to teleport or leave the plane fails.",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text("Hardened Soul",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Level 14",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("When you reach 14th level, you have advantage on saving throws against being charmed and frightened.",pad=(0,0),font=('Helvetica',10))

,sg.Text("Level 15",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Subclass Feature',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("And its rather lengthy description",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text('Level 16',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Ability Score Improvement',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.Text("Level 18",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Subclass Feature',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("And its rather lengthy description",s=(80,5),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Text('Level 19',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text('Ability Score Improvement',s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.DropDown(['Strength','Dexterity','Constitution','Intellegence','Wisdom','Charisma'],s=(25,10),readonly=True,default_value='Strength')

,sg.Text("Level 20",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Text("Sanguine Mastery",s=(45,1),pad=(0,4),font=('Helvetica',15))

,sg.Multiline("Upon reaching 20th level, your mastery of blood magic reaches its height, mitigating your sacrifice and empowering your expertise. Once per turn, whenever a blood hunter feature requires you to roll a hemocraft die, you can reroll the die and use either roll.",s=(80,3),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)

,sg.Multiline("Additionally, whenever you score a critical hit with a weapon for which you have an active crimson rite, you regain one expended use of your Blood Maledict feature.",s=(80,2),pad=(0,0),font=('Helvetica',10),disabled=True,background_color='2c2825',no_scrollbar=True,border_width=0)
]
 def rL(self):
  return self.Blood_Hunter