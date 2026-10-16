#---------------------------------------------------------
# Bash para obtener la energia total conforme cambia el
# la energia de corte "ecutwfc", y el valor de "ecutrho"
# se fija a 10x"ecutwfc", los resultados se guarda en el 
# archivo curvaEcut.dat
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

for Ecut in 10 15 20 25 30 35 40 45 50 55 60 65 70
do
echo "calculo para Ecut = $Ecut Ry"
date
Erho=`bc -l <<!
  scale=3
  10*$Ecut
!`

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
    ecutwfc = $Ecut,
    ecutrho = $Erho,
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
 10 10 10 0 0 0

!

# voy a llamar al QE
$PRE_FIX $QE -in  $name.in > $name.out   #  no leer esto 

# genero una copia del archivo de salida
cp $name.out $name_$Ecut.out   # si.scf_10.out  si.scf_15.out

# obtengo la energia del sistema
E=`grep ! $name.out | awk '{print $5}' `


echo "$Ecut  $E" >> curvaEcut.dat

done

