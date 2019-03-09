warmup_inter = [
    "Split step exercise",
    "Mirror chase",
    "Sprints",
    "High Knees",
    "Burpees",
    "Jumping Jacks",
    "6 corner movements",
    "Back V , side to side , front V and Fh toss and bkhand defence",
    "Sacche, split step and sprint",
    "High Knees and Sprint",
    "Zig Zag - sacche",
    "Zig Zag - Both legs together",
    "High plank with shoulder Tap",
    "Agility",
    "Dynamic Lunges",
    "10 Burpee , 10 mountain climber, 10 squat jumps",
    "Burpees side to side",
    "Star Jumps",
    "Squat Jumps",
    "Squat Jumps with Heel Tap and Sprint",
    "Scissor Jumps",
    "Scissor Jumps and Hit",
    "x rounds in 5 min "
    "Line touches",
    "Line Touches with Sacche",
    "Carioca",
    "Sacche and Jump",
    "Squat and 6 corners",
    "Duck walk",
    "Ankle Work",
    "One leg Jumps",
    "Bear Crawl",
    "High Knees and Sprint",
    "Rain tap (turn , down , jump , sprint)",
    "Rain tap and 6 corners",
    "Stance switch",
    "Relay Game",
    "Mountain Climbers",
    "180 degree squat jumps",
    "Skiing",
    "Plank leg in and out",
    "Throw shuttles and pickup",
    "6 corners with direction",
    "Squat jump and forward",
    "Lateral Lunges",
    "Tuck Jumps",
    "Sprints according to court",
    "Sprint according to whistle Blow",
    "A-Skips"
]

drills_inter = [
    "Centre Split and Dribble (Cone in the centre) (16 Shuttles) (Fh and Bh)",
    "Forehand Toss Action and Dribble (16 shuttles) (switch to backhand side)",
    "Centre Split and Lift (Cone in the center) (16 shuttles) (Fh and Bh)",
    "Drop Action and Lift (Straight movement) (16 shuttles) (Fh and Bh)",
    "Drop Shot, dribble , toss , lift (16 shuttles X 2) (Fh and Bh)",
    "Defence, lift , Smash (18 shuttles X 2)",
    "Tap shot Practise (20 shuttles) (Fh and Bh)",
    "Smash Tap (20 shuttles X 2) ",
    "Split and Drive Shots (20 shuttles)",
    "3 drive shots and one smash (20 shuttles X 2)",
    "Split and Defence Practise (side to side) (20 shuttles)",
    "Toss and Defence Drill OR Lift Defence Drill (20 shuttles)",
    "Split and toss shot drill (24 shuttles X 2)",
    "High Serve, toss shot , defence , dribble , smash , drive, lift (Random)",
    "Drop shot practise (Players feeding) (Overhead and Forehand)",
    "Drop shot and dribble practise (Players Feeding)",
    "Smash Shots near the net (20 X 2)",
    "SD, ST , SP, SL , SCL (25 shuttles)",
    "Serve hit catch (On the wall)",
    "Serve and Recieve (20 shuttles)",
    "Singles Match Tactics in a full court game",
    "Corner Work (with coach)",
    "Cross Court Keep shot technique",
    "Defence action and Cross Court Keep shot (20  shuttles X 2)",
    "Cross Lift Technique and Practise (Players Feed)",
    "Defence, Cross Lift, Cross Smash (18shuttles X 2)",
    "Cross Toss (20 shuttles)",
    "Cross Toss and cross keep (20shuttles X 2)",
    "Cross Court Drop shots (20shuttles X2)",
    "Cross Court Drop and cross keep (20 shuttles X 2)",
    "Cross Court Flick, wrist Movement Practise",
    "Straight , and cross flick (20 shuttles)"
]


end_drills_inter = [
    "Dribble Game",
    "Net Lift Game",
    "Drop shot, keep , dribble, lift drill (HC)",
    "Smash , defence , keep, lift drill (HC)",
    "Parallel Play (HC)",
    "High serve, toss , smash, defence , lift  (HC)",
    "Toss shots (HC)",
    "Drop shot , dribble , lift drill (HC)",
    "Smash Defence game (FC group)",
    "Full Court 11 points Game",
    "Corner Work ",
    "Cross Court Keep rallies",
    "Cross Court Game",
    "Cross Tosses",
    "Cross Drop and Cross keep drill(HC)",
    "2 vs 1 (Straight drop , cross flick, cross drop, straight flick) (Fh and Bh) (FC)"
]


day_counter_inter = 1

comp_warmup_inter = []  # completed warmup exercises
comp_drills_inter = []  # completed basic drill exercises
comp_end_drills_inter = []  # completed end drill exercises

warmup_duration_inter = 5
basic_drill_duration_inter = 25
end_drill_duration_inter = 10

first_ele_inter = 0

week_counter_inter = 1

#--------------------------------------------------------week1--------------------------------------------------------------#

for x in range(0, 2):
    if x == 0:
        print(f"Schedule for week{week_counter_inter}: ")
    print(" ")
    print(f"Day{day_counter_inter} :")
    print(
        f"                 {warmup_inter[first_ele_inter]} duration : {warmup_duration_inter} min\n")

    print(
        f"                 {drills_inter[first_ele_inter]} duration: {basic_drill_duration_inter} min\n")
    print(
        f"                 {drills_inter[first_ele_inter+1]} duration: {basic_drill_duration_inter} min\n")

    print(
        f"                 {end_drills_inter[first_ele_inter]} duration: {end_drill_duration_inter} min\n")
    comp_end_drills_inter.append(end_drills_inter.pop(first_ele_inter))

    comp_warmup_inter.append(warmup_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))

    #if day_counter==2:
    #   break;

    day_counter_inter += 1

#------------------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------week2--------------------------------------------------------------#
week_counter_inter += 1
day_counter_inter = 1
for x in range(0, 2):
    if x == 0:
        print(f"Schedule for week{week_counter_inter}: ")
    print(" ")
    print(f"Day{day_counter_inter} :")
    print(
        f"                 {warmup_inter[first_ele_inter]} duration : {warmup_duration_inter} min\n")

    print(
        f"                 {drills_inter[first_ele_inter]} duration: {basic_drill_duration_inter} min\n")
    print(
        f"                 {drills_inter[first_ele_inter+1]} duration: {basic_drill_duration_inter} min\n")

    print(
        f"                 {end_drills_inter[first_ele_inter]} duration: {end_drill_duration_inter} min\n")
    comp_end_drills_inter.append(end_drills_inter.pop(first_ele_inter))

    comp_warmup_inter.append(warmup_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))

    #if day_counter==2:
    #   break;

    day_counter_inter += 1

#------------------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------week3--------------------------------------------------------------#
week_counter_inter += 1
day_counter_inter = 1
for x in range(0, 2):
    if x == 0:
        print(f"Schedule for week{week_counter_inter}: ")
    print(" ")
    print(f"Day{day_counter_inter} :")
    print(
        f"                 {warmup_inter[first_ele_inter]} duration : {warmup_duration_inter} min\n")

    print(
        f"                 {drills_inter[first_ele_inter]} duration: {basic_drill_duration_inter} min\n")
    print(
        f"                 {drills_inter[first_ele_inter+1]} duration: {basic_drill_duration_inter} min\n")

    print(
        f"                 {end_drills_inter[first_ele_inter]} duration: {end_drill_duration_inter} min\n")
    comp_end_drills_inter.append(end_drills_inter.pop(first_ele_inter))

    comp_warmup_inter.append(warmup_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))

    #if day_counter==2:
    #   break;

    day_counter_inter += 1

#------------------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------week4--------------------------------------------------------------#
week_counter_inter += 1
day_counter_inter = 1
for x in range(0, 2):
    if x == 0:
        print(f"Schedule for week{week_counter_inter}: ")
    print(" ")
    print(f"Day{day_counter_inter} :")
    print(
        f"                 {warmup_inter[first_ele_inter]} duration : {warmup_duration_inter} min\n")

    print(
        f"                 {drills_inter[first_ele_inter]} duration: {basic_drill_duration_inter} min\n")
    print(
        f"                 {drills_inter[first_ele_inter+1]} duration: {basic_drill_duration_inter} min\n")

    print(
        f"                 {end_drills_inter[first_ele_inter]} duration: {end_drill_duration_inter} min\n")
    comp_end_drills_inter.append(end_drills_inter.pop(first_ele_inter))

    comp_warmup_inter.append(warmup_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))
    comp_drills_inter.append(drills_inter.pop(first_ele_inter))

    #if day_counter==2:
    #   break;

    day_counter_inter += 1

#------------------------------------------------------------------------------------------------------------------------------#
