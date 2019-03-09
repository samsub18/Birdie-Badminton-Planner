warmup_adv = [
    "Hitting Hands warmup",
    "Agility",
    "Overhead drop ,  Fh drop, cross keep action",
    "Rain tap and 6 corners",
    "China Jump Smash",
    "Back V Toss action (Partner)",
    "Sprints and Pushups (Tricep and Bicep)",
    "Diving Defence Practise",
    "Lift and Defence (with partner hand hitting)",
    "Mirror Chase",
    "Sprints and Split Step Exercise",
    ""

]

drills_adv = [
    "2 lifts and 2 pushes (20 shuttles X 2) (in order)",
    "Fh smash action, Fh dribble , Overhead smash action , bkh push (16 shuttles) (20 shutlles)",
    "Cross Drop and Cross court keep",
    "Cross Tosses",
    "Cross court Drop shot and cross keep",
    "Straight Drop shot and Dribble",
    "Hitting shot in one corner and moving to all corners (18 shuttles)",
    "Cross Court keep and Backhand Drop Shot",
    "China Jump smash, overhead one jump hit , backhand tap",
    "Ready, Touch, Smash, Tap",
    "Toss Shot, Slow Recovery",
    "Toss Shot, Slow Revcovery, Smash",
    "Backhand Toss Shot (Technique and 20 shuttlesX2)",
    "Fh dribble and Backhand Drive (20 shutlles)",
    "Defence 2 vs 1",
    "Fh Defence and Overhead Shot (20 shuttles)",
    "Lift and Defence Practise (20 shuttles)",
    "2 vs 1 Defence Practise",
    "Side to Side Smash(20 Shuttles) (Players Feeding)",
    "Fh Cross Drop, Overhead Action and Bkh dribble (15 times)"

]

end_drills_adv = [
    "Net Lift Game",
    "Cross Court Game",
    "Dribble game",
    "Tag Game",
    "Calf Touching",
    "Toss Shots with Slow recovery (HC)",
    "Backhand Drop Shot and Keep (HC)",
    "HC game , where one attacks and one defends",
    "Bending Knees and Defence Drill (with tennis ball) and LD Defence Exercise",
    "Doubles Rotation HC game"
]

day_counter_adv = 1
week_counter_adv = 1
batch_counter = 1
first_drill = 0

warmup_dur_adv = 5
drill_dur_adv = 25
end_drill_dur_adv = 10

comp_drills_adv = []
comp_warmup_adv = []
comp_end_drills_adv = []


#------------------------------------------------week1--------------------------------------------------------------------#
for x in range(0, 5):
    if x == 0:
        print(f"Schedule for week{week_counter_adv}: ")
        print(" ")
        print(" ")

    if x == 0 or x == 1 or x == 2:

        print(f"Day{day_counter_adv}: ")
        print(" ")
        print(" ")

        for _ in range(0, 2):

            print(f"      Batch{batch_counter}: ")
            print(
                f"                    {warmup_adv[first_drill]} duration: {warmup_dur_adv}min")
            print(
                f"                    {drills_adv[first_drill]} duration: {drill_dur_adv}min")
            print(
                f"                    {drills_adv[first_drill+1]} duration: {drill_dur_adv}min")
            print(
                f"                    {end_drills_adv[first_drill]} duration: {end_drill_dur_adv}min")
            batch_counter += 1
            comp_warmup_adv.append(warmup_adv.pop(first_drill))
            comp_drills_adv.append(drills_adv.pop(first_drill))
            comp_drills_adv.append(drills_adv.pop(first_drill))
            comp_end_drills_adv.append(end_drills_adv.pop(first_drill))
        day_counter_adv += 1
        batch_counter = 1

    else:
        print(f"Day{day_counter_adv}: ")
        print(
            f"                    {warmup_adv[first_drill]} duration: {warmup_dur_adv}min")
        print(
            f"                    {drills_adv[first_drill]} duration: {drill_dur_adv}min")
        print(
            f"                    {drills_adv[first_drill+1]} duration: {drill_dur_adv}min")
        print(
            f"                    {end_drills_adv[first_drill]} duration: {end_drill_dur_adv}min")
        day_counter_adv += 1
        comp_warmup_adv.append(warmup_adv.pop(first_drill))
        comp_drills_adv.append(drills_adv.pop(first_drill))
        comp_drills_adv.append(drills_adv.pop(first_drill))
        comp_end_drills_adv.append(end_drills_adv.pop(first_drill))
#----------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------week2-----------------------------------------------------------------#
print(" ")
print(" ")

week_counter_adv += 1
batch_counter = 1
day_counter_adv = 1

for x in range(0, 5):
    if x == 0:
        print(f"Schedule for week{week_counter_adv}: ")
        print(" ")
        print(" ")

    if x == 0 or x == 1 or x == 2:

        print(f"Day{day_counter_adv}: ")
        print(" ")
        print(" ")

        for _ in range(0, 2):

            print(f"      Batch{batch_counter}: ")
            print(
                f"                    {warmup_adv[first_drill]} duration: {warmup_dur_adv}min")
            print(
                f"                    {drills_adv[first_drill]} duration: {drill_dur_adv}min")
            print(
                f"                    {drills_adv[first_drill+1]} duration: {drill_dur_adv}min")
            print(
                f"                    {end_drills_adv[first_drill]} duration: {end_drill_dur_adv}min")
            batch_counter += 1
            comp_warmup_adv.append(warmup_adv.pop(first_drill))
            comp_drills_adv.append(drills_adv.pop(first_drill))
            comp_drills_adv.append(drills_adv.pop(first_drill))
            comp_end_drills_adv.append(end_drills_adv.pop(first_drill))
        day_counter_adv += 1
        batch_counter = 1

    else:
        print(f"Day{day_counter_adv}: ")
        print(
            f"                    {warmup_adv[first_drill]} duration: {warmup_dur_adv}min")
        print(
            f"                    {drills_adv[first_drill]} duration: {drill_dur_adv}min")
        print(
            f"                    {drills_adv[first_drill+1]} duration: {drill_dur_adv}min")
        print(
            f"                    {end_drills_adv[first_drill]} duration: {end_drill_dur_adv}min")
        day_counter_adv += 1
        comp_warmup_adv.append(warmup_adv.pop(first_drill))
        comp_drills_adv.append(drills_adv.pop(first_drill))
        comp_drills_adv.append(drills_adv.pop(first_drill))
        comp_end_drills_adv.append(end_drills_adv.pop(first_drill))

#-----------------------------------------------------------------------------------------------------------------------------#
