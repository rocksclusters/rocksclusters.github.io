#!/bin/bash
#
#$ -cwd
#$ -j y
#$ -S /bin/bash
#
MPI_DIR=/opt/mpich/gnu
                                                                                
$MPI_DIR/bin/mpirun -np $NSLOTS -machinefile $TMPDIR/machines \
        /opt/hpl/gnu/bin/xhpl

