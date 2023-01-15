package routes

import (
	controller "kriptoloji/controllers"
	"kriptoloji/middlewares"

	"github.com/gin-gonic/gin"
)

// UserRoutes function
func UserRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.Use(middlewares.Authentication())
	incomingRoutes.GET("/users/:user_id", controller.GetUser())
}
