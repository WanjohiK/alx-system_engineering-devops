#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method
# Repetition Token #3

# puts ARGV[0].scan(/^hbt+n/).join
puts ARGV[0].scan(/hbt*n/).join
