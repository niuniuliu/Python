x = gets.chomp.to_i

# until x < 0
#     puts x
#     x -= 1
# end

# puts "Done!"


# while x >= 0
#     puts x
#     x -= 1
# end

# puts "Done!"

begin
    
    puts "Do you want to do that again?"
    answer = gets.chomp
    puts "Your answer is #{answer}"
    
end while answer == 'Y'
