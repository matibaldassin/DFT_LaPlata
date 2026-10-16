#---------------------------------------------------------
# Bash para obtener la energia total conforme cambia el 
# parametro de red, y lo guarda en el archivo curvaA.dat
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

for a in 5.30 5.32 5.34 5.36 5.38 5.40 5.42 5.44 5.46 5.48 5.50 5.52 5.54 5.56 5.58 5.60
do
date
echo "calculo para a = $a A"
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
    a = $a, 
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
 Si  28.086 Si.pbe-n-rrkjus_psl.0.1.UPF 
ATOMIC_POSITIONS {crystal}
 Si 0.00 0.00 0.00
 Si 0.25 0.25 0.25
K_POINTS {automatic}
 12 12 12 0 0 0

!

$PRE_FIX $QE -in  $name.in > $name.out

E=`grep ! $name.out | awk '{print $5}' `

echo "$a  $E" >> curvaA.dat

done

