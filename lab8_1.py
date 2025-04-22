21, 28, 72, 41, 93, 68, 45, 78, 5

# SELECTION SORT STEPS
[21, 28, 72, 41, 93, 68, 45, 78, 5]
# smallest unsorted number 5
[5, 28, 72, 41, 93, 68, 45, 78, 21]
# smallest unsorted number 21
[5, 21, 72, 41, 93, 68, 45, 78, 28]
# smallest unsorted number 28
[5, 21, 28, 41, 93, 68, 45, 78, 72]
# smallest unsorted number 41
[5, 21, 28, 41, 93, 68, 45, 78, 72]
# smallest unsorted number 45
[5, 21, 28, 41, 45, 68, 93, 78, 72]
# smallest unsorted number 68
[5, 21, 28, 41, 45, 68, 93, 78, 72]
# smallest unsorted number 72
[5, 21, 28, 41, 45, 68, 72, 78, 93]
# smallest unsorted number 78
[5, 21, 28, 41, 45, 68, 72, 78, 93]
# smallest unsorted number 93
[5, 21, 28, 41, 45, 68, 72, 78, 93]

#-----------------------------------------------------------

# INSERTION SORT STEPS
[21, 28, 72, 41, 93, 68, 45, 78, 5]
# compare 28 to 21. 28 is larger. no shift
[21, 28, 72, 41, 93, 68, 45, 78, 5]
# compare 72 to 28. 72 is larger. no shift
[21, 28, 72, 41, 93, 68, 45, 78, 5]
# compare 41 to 72. 41 is smaller. shift 72
# compare 41 to 28. 41 is larger. insert here
[21, 28, 41, 72, 93, 68, 45, 78, 5]
# compare 93 to 72. 93 is larger. no shift
[21, 28, 41, 72, 93, 68, 45, 78, 5]
# compare 68 to 93. 68 is smaller. shift 93
# compare 68 to 72. 68 is smaller. shift 72
# compare 68 to 41. 68 is larger. insert here
[21, 28, 41, 68, 72, 93, 45, 78, 5]
# compare 45 to 93. 45 is smaller. shift 93
# compare 45 yo 72. 45 is smaller. shift 72
# compare 45 to 68. 45 is smaller. shift 68
# compare 45 to 41. 45 is larger. insert here
[21, 28, 41, 45, 68, 72, 93, 78, 5]
# compare 78 to 93. 78 is smaller. shift 93
# compare 78 to 72. 78 is larger. insert here
[21, 28, 41, 45, 68, 72, 78, 93, 5]
# compare 93 to 78. 83 is larger. no shift
[21, 28, 41, 45, 68, 72, 78, 93, 5]
# compare 5 to 93. 5 is smaller. shift 93
# compare 5 to 78. 5 is smaller. shift 78
# compare 5 to 72. 5 is smaller. shift 72
# compare 5 to 68. 5 is smaller. shift 68
# compare 5 to 45. 5 is smaller. shift 45
# compare 5 to 41. 5 is smaller. shift 41
# compare 5 to 28. 5 is smaller. shift 28
# compare 5 to 21. 5 is smaller. shift 21
# insert 5 at index 0
[5, 21, 28, 41, 45, 68, 72, 78, 93]

#----------------------------------------------------------

# BUBBLE SORT STEPS
[21, 28, 72, 41, 93, 68, 45, 78, 5]

# PASS 1
# compare 21 to 28. correct. no swap
# compare 28 to 72. correct. no swap 
# compare 72 to 41. larger. swap
[21, 28, 41, 72, 93, 68, 45, 78, 5]
# compare 72 to 93. correct. no swap 
# compare 93 to 68. larger. swap
[21, 28, 41, 72, 68, 93, 45, 78, 5]
# compare 93 to 45. larger. swap
[21, 28, 41, 72, 68, 45, 93, 78, 5]
# compare 93 to 78. larger. swap 
[21, 28, 41, 72, 68, 45, 78, 93, 5]
# compare 93 to 5. larger. swap
[21, 28, 41, 72, 68, 45, 78, 5, 93]

# PASS 2
[21, 28, 41, 72, 68, 45, 78, 5, 93]
# compare 21 to 28. correct. no swap
# compare 28 to 41. correct. no swap 
# compare 41 to 72. correct. no swap
# compare 72 to 68. larger. swap
[21, 28, 41, 68, 72, 45, 78, 5, 93]
# compare 72 to 45. larger. swap 
[21, 28, 41, 68, 45, 72, 78, 5, 93]
# compare 72 to 78. correct. no swap
# compare 78 to 5. larger. swap
[21, 28, 41, 68, 45, 72, 5, 78, 93]
# compare 78 to 93. correct. no swap

# PASS 3 
[21, 28, 41, 68, 45, 72, 5, 78, 93]
# compare 21 to 28. correct. no swap 
# compare 28 to 41. correct. no swap 
# compare 41 to 68. correct. no swap
# compare 68 to 45. wrong. swap
[21, 28, 41, 45, 68, 72, 5, 78, 93]
# compare 68 to 72. correct. no swap 
# compare 72 to 5. wrong. swap
[21, 28, 41, 45, 68, 5, 72, 78, 93]
# compare 72 to 78. correct. no swap
# compare 78 to 93. correct. no swap
[21, 28, 41, 45, 68, 5, 72, 78, 93]

# PASS 4 
[21, 28, 41, 45, 68, 5, 72, 78, 93]
# compare 21 to 28. correct. no swap
# compare 28 to 41. correct. no swap 
# compare 41 to 45. correct. no swap
# compare 45 to 68. correct. no swap
# compare 68 to 5. wrong. swap
[21, 28, 41, 45, 5, 68, 72, 78, 93]
# compare 68 to 72. correct. no swap
# compare 72 to 78. correct. no swap 
# compare 78 to 93. correct. no swap

# PASS 5 
[21, 28, 41, 45, 5, 68, 72, 78, 93]
# compare 21 to 28. correct. no swap
# compare 28 to 41. correct. no swap 
# compare 41 to 45. correct. no swap
# compare 45 to 5. wrong. swap
[21, 28, 41, 5, 45, 68, 72, 78, 93]
# compare 45 to 68. correct. no swap
# compare 68 to 72. correct. no swap
# compare 72 to 78. correct. no swap 
# compare 78 to 93. correct. no swap

#----------------------------------------------------------

# MERGE SORT STEPS
