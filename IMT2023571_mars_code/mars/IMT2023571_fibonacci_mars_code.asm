.data 
	x: .word 15
.text
	addi $t4,$t4,0
	lw $s0,0($t4)
	addi $t0,$zero,0
	addi $t1,$zero,1
	addi $t2,$zero,0
	addi $t3,$s0,-1
	beq $s0,$t0,loop1
	beq $s0,$t1,loop2
	bne $t3,$t2,loop
	
	loop1:
		sw $t0,4($t4)
		li $v0,10
		syscall
	loop2:
		addi $t0,$t1,0
		sw $t0,4($t4)
		li $v0,10
		syscall
	loop:
		add $s1,$t0,$t1
		addi $t0,$t1,0
		addi $t1,$s1,0
		addi $t2,$t2,1
		bne $t3,$t2,loop
		addi $t0,$s1,0
		sw $t0,4($t4)
		li $v0,10
		syscall		
		
		
		
	
