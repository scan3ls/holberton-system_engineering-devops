#!/usr/bin/env ruby
var = ARGV[0].scan(/(from:.*\])|(to:.*\])|(flags:.*\])/).join
list = var.split("]")
list[0].slice!("from:")
from = list[0]
list[1].slice!(" [to:")
to = list[1]
list[2].slice!(" [flags:")
flags = list[2]
string = "%s,%s,%s" % [from, to, flags]
puts string
