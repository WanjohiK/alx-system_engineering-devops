#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method

# puts ARGV[0].scan(/hbtt{1,4}n/).join
# puts ARGV[0].scan(/hbt{2,5}n/).join
puts ARGV[0].scan(/^hbt{2,5}n/).join
