=begin

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

Input: array of reports (nums), report is a list of nums called levels (space separated)
Output: number of valid reports

valid reports have all increasing or all decreasing nums
valid report levels differ by at least 1 and most 3 (number/level can't repeat)


EXAMPLES
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

DATA STRUCTURE
- array of arrays
- each report is an array of nums (levels)

ALGORITHM
parse input
- create array of reports from input

count valid reports


check valid report
all increasing
all decreasing
adjecent level check

=end

def parse_input(file)
  lines = File.readlines(file)
  lines.map { |line| line.split(' ').map(&:to_i)}
end

def all_increasing?(report)
  report.each_with_index do |level, i|
    next if i == 0
    return false if report[i] < report[i - 1]
  end
  true
end

def all_decreasing?(report)
  report.each_with_index do |level, i|
    next if i == 0
    return false if report[i] > report[i - 1]
  end
  true
end


def valid_level_difference(report)
  i = 1
  loop do
    difference = (report[i] - report[i - 1]).abs
    i += 1
    return false if difference > 3 || difference <= 0
    break if i >= report.size
  end
  true
end

def problem_dampener(report)
  report.map.with_index do |level, i|
    dupped = report.dup
    dupped.delete_at(i)
    dupped
  end
end

# p problem_dampener([7, 6, 4, 2, 1])

def valid_report(report)
  (all_decreasing?(report) || all_increasing?(report)) && valid_level_difference(report)
end

def count_valid_reports(reports)
  valid_reports = 0

  reports.each do |report|
    valid_reports += 1 if problem_dampener(report).any? { |report| valid_report(report)}
  end

  valid_reports
end
# reports = parse_input('./day2_test_input.txt')
reports = parse_input('./day2_input.txt')
p count_valid_reports(reports)

