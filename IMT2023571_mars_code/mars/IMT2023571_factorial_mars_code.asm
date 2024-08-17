.data
 	x: .word 7
.text
	addi $t3,$t3,0
	lw $s0,0($t3)
	addi $t0,$zero,1
	addi $t1,$zero,1
	addi $t2,$zero,0
	beq $t2,$s0 ,exit
	
	bne $t2,$s0,loop
	loop:
		mul $t1,$t1,$t0
		addi $t0,$t0,1
		addi $t2,$t2,1
		bne $t2,$s0,loop
		sw $t1 4($t3)
		li $v0,10
		syscall
	exit: 
		sw $t1 4($t3)
		li $v0,10
		syscall
		
