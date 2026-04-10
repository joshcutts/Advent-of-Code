def parse_input(file)
  content = File.read(file)
  content
end

def expand(dense)
  expanded = []
  id = 0

  dense.to_s.chars.each_with_index do |char, i|
    if i % 2 == 0
      char.to_i.times {expanded.push(id)}
      id += 1
    else
      char.to_i.times {expanded.push(nil)}
    end
  end

  expanded
end

# p expand(12345)

def find_free_spaces(expanded)
  expanded.map.with_index { |char, i| i if !char}.compact
end

# p find_free_spaces(expand(12345))
# 

=begin

- find all the nil indices
- iterate from the back (reverse each, with index)
- swap nil index and back index
- increment nil index
- break if back index < nil index

=end

def compact_file(expanded)
  free_spaces = find_free_spaces(expanded)
  free_index = 0

  expanded.reverse_each.with_index do |id, reverse_i|
    next if !id
    empty_index = free_spaces[free_index]
    i = expanded.size - reverse_i - 1

    break if i <= empty_index
    expanded[empty_index], expanded[i] = expanded[i], expanded[empty_index]
    free_index += 1    
  end
  expanded
end

expanded_ex = expand('2333133121414131402')
p find_free_spaces(expanded_ex)
# expanded_ex = expand(File.read('./day9_intput.txt'))
# p expanded_ex
compacted_file = compact_file(expanded_ex)
# p compacted_file.compact.each_with_index.sum { |id, i| id * i}
# p compacted_file.compact.sum.with_index { |num, i| num * i}'
# 

=begin


- Iterate through the array backwards
- find the length of the same element (not nil)
- look for an empty space equal to or less than the current length
- check for spaces from the front of the array
- if there is a space
  - replace with the elements from the end of the array

=end

# p Array.new(3, 9)
# 
#
def find_contiguous_length(expanded, index)
  length = 1
  
  while expanded[index] == expanded[index - 1]
    length += 1
    index -= 1
  end

  return length
end

expanded = [0, 0, nil, nil, nil, 1, 1, 1, nil, nil, nil, 2, nil, nil, nil, 3, 3, 3, nil, 4, 4, nil, 5, 5, 5, 5, nil, 6, 6, 6, 6, nil, 7, 7, 7, nil, 8, 8, 8, 8, 9, 9]

# p find_contiguous_length(expanded, expanded.size - 3)

def find_first_open_space(expanded, size, stop_index)
  nil_length = 0

  expanded.each_with_index do |id, index|
    return nil if index >= stop_index

    if id.nil?
      nil_length += 1
      return index - nil_length + 1 if nil_length >= size
    else
      nil_length = 0
    end
  end

  nil
end

# p find_first_open_space(expanded, 1)

# p find_free_spaces_obj(expanded)

def compact_contig(expanded)
  r = expanded.size - 1

  while r > 0
    current_id = expanded[r]
    # p "#{current_id}, #{r}, #{expanded.size}"
    if !current_id
      r -= 1
      next
    end

    contiguous_length = find_contiguous_length(expanded, r)
    empty_index = find_first_open_space(expanded, contiguous_length, r - contiguous_length + 1)
    
    if empty_index
      expanded[empty_index...empty_index + contiguous_length] = Array.new(contiguous_length, current_id)
      expanded[r - contiguous_length + 1..r] = Array.new(contiguous_length, nil)
    end
    # p expanded
    r -= contiguous_length
  end

  return expanded
end

# contig_compacted_file = compact_contig(expanded)
contig_compacted_file = compact_contig(expand(File.read('./day9_input.txt')))

p contig_compacted_file.each_with_index.sum { |id, i| id.to_i * i}
# 15616542779939 too high