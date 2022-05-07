package board

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHello(t *testing.T) {
	friendly := hello()
	assert.Equal(t, friendly, true, "Code is not being friendly! Expected true")
}
