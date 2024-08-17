.data
 	x: .word -2
	n: .word 3
.text
	addi $t0,$t0,0
	lw $s1,0($t0)
	lw $s2,4($t0)
	addi $s0,$zero,1
	addi $t1,$zero,0
	bne $t1,$s2,loop
	sw $s0,8($t0)
	li $v0,10
	syscall
	loop:
	mul $s0,$s0,$s1
	addi $t1,$t1,1
	bne $t1,$s2,loop
	sw $s0,8($t0)
	li $v0,10
	syscall
	
	