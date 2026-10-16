#---------------------------------------------------------
# Bash para obtener la energia total conforme cambia el
# numero de k-points, los resultados se # guarda en el 
# archivo curvaK.dat
#
# Dr. Arles V. Gil Rebaza
# Dpto. de Fisica, Fac. de Ciencias Exactas de la UNLP
# Instituto de Fisica La Plata, IFLP - CONICET
# GEMyDE - Fac. de Ingenieria de la UNLP
#---------------------------------------------------------

#!/bin/bash
PRE_FIX="mpirun -np 2"
QE="pw.x"

name=si.scf

for k in 4 6 8 10 12 14 16 18 20
do
date
#Erho=`bc -l <<!
#  scale=3
#  40*$a
#!`
echo "calculo para K-points: $k $k $k"
cat > $name.in <<!
&control
    calculation = 'scf'
    restart_mode='from_scratch',
    prefix='silicon',
    tstress = .true.
    tprnfor = .true.
    pseudo_dir = './',
    outdir='./'
 /
 &system
    ibrav=  2, 
    a = 5.43, 
    nat=  2, ntyp= 1,
    ecutwfc = 40,
    ecutrho = 400,
    nbnd=8,
    occupations='fixed',
 /
 &electrons
    mixing_mode = 'plain'
    mixing_beta = 0.5
    conv_thr =  1.0d-10
 /
ATOMIC_SPECIES
 Si  28.086  Si.pbe-n-rrkjus_psl.0.1.UPF
ATOMIC_POSITIONS {crystal}
 Si 0.00 0.00 0.00
 Si 0.25 0.25 0.25
K_POINTS {automatic}
 $k $k $k 0 0 0

!

$PRE_FIX $QE -in  $name.in > $name.out

E=`grep ! $name.out | awk '{print $5}' `

echo "$k  $E" >> curvaK.dat

done

