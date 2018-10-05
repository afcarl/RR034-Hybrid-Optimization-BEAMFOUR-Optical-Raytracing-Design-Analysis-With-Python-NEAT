"""
1-input BEAM4 example -- this is most likely the simplest possible example.
"""

from __future__ import print_function
import os
import sys
import neat
import visualize
from shutil import copyfile

# 2-input XOR inputs and expected outputs.
#xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
xor_inputs = [(1.0)]
#xor_outputs = [   (0.0,),     (1.0,),     (1.0,),     (0.0,)]

best_fitness_so_far = -99999.0


#def eval_genome( genome_id , genome , config ):
def eval_genome( genome_id , genome , config , winner_flag ):
    global best_fitness_so_far
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    output = net.activate( xor_inputs )
    output_a = min( 1.0 , output[0] )
    output_aa = max( 0.0 , output_a )

    if os.path.exists( "INPUT.OPT" ) and os.path.isfile( "INPUT.OPT" ) and not( os.stat( "INPUT.OPT" )[6]==0 ):
        os.remove("INPUT.OPT")

    if os.path.exists( "INPUT.RAY" ) and os.path.isfile( "INPUT.RAY" ) and not( os.stat( "INPUT.RAY" )[6]==0 ):
        os.remove("INPUT.RAY")

    if os.path.exists( "BEAM4_DONE.out" ) and os.path.isfile( "BEAM4_DONE.out" ) and not( os.stat( "BEAM4_DONE.out" )[6]==0 ):
        os.remove("BEAM4_DONE.out")

    Pitch_1_min = 5.0
    Pitch_1_max = 80.0

    x1 = 0.0
    y1 = Pitch_1_min
    x2 = 1.0
    y2 = Pitch_1_max

    Pitch_y = y2 + ( y1 - y2 ) / ( x1 - x2 ) * ( output_aa - x2 )
    #print( output[0], output_a, output_aa , Pitch_y )

    INPUT_OPT = []
    INPUT_OPT.append( " 3 surfaces INPUT.OPT (RMS=x.xxx)" )
    INPUT_OPT.append( "   X         Y         Z       Pitch :   type?     Diam     OffOx      Curv     Asph     f" )
    INPUT_OPT.append( "--------:---------:---------:---------:--------:---------:---------:---------:---------:----:--" )
    INPUT_OPT.append( "   0    :   0.0   :    6.3  :  22.2423? Mirror :         :         :  -0.1670: -70.1537: S  :" )
    INPUT_OPT.append( "   0    :   0.0   :   -5.0  :-201.2879: Mirror :         :         :  -0.0440:  -0.0007:    :" )
    INPUT_OPT.append( "   0    :   0.0   :   50.0  :    0    :        :   100   :         :    0    :    0    :    :" )

    INPUT_OPT_input = open( "INPUT.OPT" , "w" )
    INPUT_OPT_input.write( INPUT_OPT[0] + '\n' )
    INPUT_OPT_input.write( INPUT_OPT[1] + '\n' )
    INPUT_OPT_input.write( INPUT_OPT[2] + '\n' )
    INPUT_OPT_input.write( "   0    :   0.0   :    6.3  :" + "{0:<9.8g}".format( Pitch_y )[:9] + "? Mirror :         :         :  -0.1670: -70.1537: S  :" + '\n' )
    INPUT_OPT_input.write( INPUT_OPT[4] + '\n' )
    INPUT_OPT_input.write( INPUT_OPT[5] + '\n' )
    INPUT_OPT_input.close()

    #copyfile( "SOURCE_a.OPT" , "INPUT.OPT" )
    copyfile( "SOURCE_a.RAY" , "INPUT.RAY" )
    #sys.exit(0)

    os.system("BEAM4_d2.exe")

    INPUT_OPT_input = open( "INPUT.OPT" , "r" )
    test_INPUT_OPT_input = INPUT_OPT_input.readline()	# read 1st line: " 3 surfaces INPUT.OPT (RMS=x.xxx)"
    test_INPUT_OPT_input = INPUT_OPT_input.readline()	# read 2nd line: "   X         Y         Z       Pitch :   type?     Diam     OffOx      Curv     Asph     f"
    test_INPUT_OPT_input = INPUT_OPT_input.readline()	# read 3rd line: "--------:---------:---------:---------:--------:---------:---------:---------:---------:----:--"
    test_INPUT_OPT_input = INPUT_OPT_input.readline()	# read 4th line: "   0    :   0.0   :    6.3  :  22.2423? Mirror :         :         :  -0.1670: -70.1537: S  :"
    list_tmp = []
    list_tmp = test_INPUT_OPT_input.replace("  "," ").replace("  "," ").replace("  "," ").replace(" ","").replace("?",":").strip('\n').split(":")
    INPUT_OPT_input.close()
    #print( list_tmp )
    #sys.exit(0)

    # check for out of bounds as a consequence of built-in non-constrained optimization
    Pitch_1 = float( list_tmp[3] )
    out_of_bounds_flag = 0
    if ( Pitch_1 < Pitch_1_min ) or ( Pitch_1 > Pitch_1_max ):
        out_of_bounds_flag = 1

    # Set genome fitness
    if out_of_bounds_flag == 0:
        BEAM4_DONE_input = open( "BEAM4_DONE.out" , "r" )
        test_BEAM4_DONE_input = BEAM4_DONE_input.readline()	# read 1st line: Done
        test_BEAM4_DONE_input = BEAM4_DONE_input.readline()	# read 2nd line: Iteration = 6
        test_BEAM4_DONE_input = BEAM4_DONE_input.readline()	# read 3rd line: RMS Average =    7.25E00
        list_tmp = []
        list_tmp = test_BEAM4_DONE_input.replace("  "," ").replace("  "," ").replace("  "," ").strip('\n').split(" ")
        RMS_error = float( list_tmp[-1] )
        test_BEAM4_DONE_input = BEAM4_DONE_input.readline()	# read 4th line: Nrays = 639
        BEAM4_DONE_input.close()
        list_tmp = []
        list_tmp = test_BEAM4_DONE_input.replace("  "," ").replace("  "," ").replace("  "," ").strip('\n').split(" ")
        N_good_RAYS = float( list_tmp[-1] )
        #r_bottom = ( RMS_error * N_good_RAYS / 656.0 )
        if N_good_RAYS == 0:
            N_good_RAYS = 0.001
        r_bottom = ( RMS_error * 656.0 / N_good_RAYS )
        if r_bottom == 0:
            r_bottom = 999999.0
        genome.fitness = 1.0 / r_bottom
        #print( list_tmp )
        #print( genome.fitness )
        #sys.exit(0)
    else:
        genome.fitness = 1.0 / 999999.0

    # check for best fitness so far and write files if appropriate
    if genome.fitness > best_fitness_so_far:
        best_fitness_so_far = genome.fitness
        print( "New best_fitness_so_far = ", best_fitness_so_far , genome_id )
        copyfile( "INPUT.OPT" , ".\\0_RESULTS\\BESTSOFAR_INPUT_" + str( genome_id ) + ".OPT" )
        copyfile( "INPUT.RAY" , ".\\0_RESULTS\\BESTSOFAR_INPUT_" + str( genome_id ) + ".RAY" )
        copyfile( "BEAM4_DONE.out" , ".\\0_RESULTS\\BESTSOFAR_BEAM4_DONE_" + str( genome_id ) + ".OUT" )

    # check to see if this a winner evaluation, and write files if appropriate
    if winner_flag == 0:
        copyfile( "INPUT.OPT" , ".\\0_RESULTS\\INPUT_" + str( genome_id ) + ".OPT" )
        copyfile( "INPUT.RAY" , ".\\0_RESULTS\\INPUT_" + str( genome_id ) + ".RAY" )
        copyfile( "BEAM4_DONE.out" , ".\\0_RESULTS\\BEAM4_DONE_" + str( genome_id ) + ".OUT" )
    else:
        copyfile( "INPUT.OPT" , ".\\0_RESULTS\\WINNER_INPUT" + ".OPT" )
        copyfile( "INPUT.RAY" , ".\\0_RESULTS\\WINNER_INPUT" + ".RAY" )
        copyfile( "BEAM4_DONE.out" , ".\\0_RESULTS\\WINNER_BEAM4_DONE" + ".OUT" )





def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        #eval_genome( genome_id , genome , config )
        winner_flag = 0
        eval_genome( genome_id , genome , config , winner_flag )

def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 300 generations.
    #winner = p.run(eval_genomes, 300)
    winner = p.run(eval_genomes, 2 )

    winner_flag = 1
    genome_id = 999999
    eval_genome( genome_id , winner , config , winner_flag )

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    #for xi, xo in zip(xor_inputs, xor_outputs):
    #    output = winner_net.activate(xi)
    #    print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
    output = winner_net.activate(xor_inputs)
    #xo = 0.5
    #print("input {!r}, expected output {!r}, got {!r}".format(xor_inputs, xo, output))

    #node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    #visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    #p.run(eval_genomes, 10)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config_test')
    run(config_path)
