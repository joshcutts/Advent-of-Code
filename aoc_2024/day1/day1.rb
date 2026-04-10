=begin

3   4
4   3
2   5
1   3
3   9
3   3

1. get array of col1 and col2
2. sort each
3. iterate through and find distances
4. sum distances

=end

def parse_input(file)
  lines = File.readlines(file)
  arr1 = []
  arr2 = []

  lines.each do |line|
    line_arr = line.split(' ')
    arr1.push(line_arr[0].to_i)
    arr2.push(line_arr[1].to_i)
  end

  [arr1.sort, arr2.sort]
end

def calculate_distance(arr)
  arr1, arr2 = arr
  distance_sum = 0

  arr1.each_with_index { |_, i| distance_sum += (arr1[i] - arr2[i]).abs}

  distance_sum
end

arrays = parse_input('./day1_input.txt')
p calculate_distance(arrays)