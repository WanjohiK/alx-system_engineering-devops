#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method
#Repetition Token #1
# puts ARGV[0].scan(/hb?tn/).join

puts ARGV[0].scan(/^hb?tn/).join
