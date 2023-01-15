package routes

import (
	controller "kriptoloji/controllers"

	"github.com/gin-gonic/gin"
)

// UserRoutes function
func AuthRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.POST("/signup", controller.SignUp())
	incomingRoutes.POST("/login", controller.Login())
}
