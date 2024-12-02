package part1

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func Result() int {
	reader := bufio.NewReader(os.Stdin)
	count := 0
outer:
	for {
		l, _, err := reader.ReadLine()
		if err != nil {
			break
		}
		nums := strings.Split(string(l), " ")
		prev, _ := strconv.Atoi(nums[1])
		prevprev, _ := strconv.Atoi(nums[0])
		diff := prev - prevprev
		if diff > 3 || diff < -3 {
			continue outer
		}
		for _, i := range nums[2:] {
			current, _ := strconv.Atoi(i)
			diffc := current - prev
			if diffc*diff <= 0 || diffc > 3 || diffc < -3 {
				continue outer
			}
			diff = diffc
			prev = current
		}
		count++

	}
	return count
}
