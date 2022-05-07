package board

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestEmpty(t *testing.T) {
	assert.Equal(t, isEmpty(), true, "Expecting board to be empty by default")
}
