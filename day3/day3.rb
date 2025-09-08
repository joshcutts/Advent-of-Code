sample_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def parse_input(file)
  raw_input = File.read(file)
  raw_input.scan(/mul\((\d+),(\d+)\)/).map { |arr| arr.map(&:to_i)}
end

p parse_input('./day3_sample_input.txt')

def sum_multiplications(array)
  array.reduce(0) { |sum, (a, b)| sum + (a * b)}
end

nums = parse_input('./day3_input.txt')
p sum_multiplications(nums)

# part 2
# sample2_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def do_parse(file)
  raw = File.read(file)
  re  = /(?<ctrl>don't|do)\(\)|mul\((?<a>\d+),(?<b>\d+)\)/

  unfiltered = raw.scan(re).map do |ctrl, a, b|
    ctrl ? ctrl : [a.to_i, b.to_i]
  end

  capture = true
  unfiltered.select do |value|
    if value.is_a?(Array) && capture
      true
    else
      capture = value == 'do' ? true : false
      false
    end
  end
end

new_parsed = do_parse('./day3_input.txt')
p sum_multiplications(new_parsed)
