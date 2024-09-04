#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.length != 1
  puts "Usage: ruby match_school.rb <string>"
  exit 1
end

# Assign the argument to a variable
input = ARGV[0]

# Define the regular expression
regexp = /School/

# Match the input string against the regular expression
if input.match?(regexp)
  puts "Match found: #{input}"
else
  puts "No match found."
end
