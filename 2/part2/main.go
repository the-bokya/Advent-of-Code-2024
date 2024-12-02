package part2

import (
	"bufio"
	"os"
	"slices"
	"strconv"
	"strings"
)

func Result() int {
	reader := bufio.NewReader(os.Stdin)
	count := 0
	for {
		l, _, err := reader.ReadLine()
		if err != nil {
			break
		}
		nums := strings.Split(string(l), " ")
	inner:
		for i := -1; i < len(nums); i++ {
			nums_ := make([]string, 0)
			if i == -1 {
				nums_ = nums
			} else {
				nums_ = slices.Concat(nums[:i], nums[i+1:])
			}
			prev, _ := strconv.Atoi(nums_[1])
			prevprev, _ := strconv.Atoi(nums_[0])
			diff := prev - prevprev
			if diff > 3 || diff < -3 {
				continue inner
			}
			for _, i := range nums_[2:] {
				current, _ := strconv.Atoi(i)
				diffc := current - prev
				if diffc*diff <= 0 || diffc > 3 || diffc < -3 {
					continue inner
				}
				diff = diffc
				prev = current
			}
			count++
			break
		}

	}
	return count
}
