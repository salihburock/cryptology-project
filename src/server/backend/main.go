package main

import (
	"net/http"
	"net/url"
	"os"

	routes "kriptoloji/routes"

	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
	"github.com/gin-gonic/gin"
	_ "github.com/heroku/x/hmetrics/onload"
)

func checkSession(c *gin.Context) {
	session := sessions.Default(c)

	if session.Get("user_id") == nil {
		location := url.URL{Path: "/login"}
		c.Redirect(http.StatusFound, location.RequestURI())
	}
}
func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "5500"
	}
	router := gin.New()
	router.Use(gin.Recovery(), gin.Logger())

	router.Static("/static", "./static")
	router.LoadHTMLGlob("templates/*")

	store := cookie.NewStore([]byte("secret"))
	router.Use(sessions.Sessions("session", store))

	router.GET("/getuser", func(c *gin.Context) {
		checkSession(c)
		session := sessions.Default(c)

		c.JSON(http.StatusOK, gin.H{"user_id": session.Get("user_id")})
	})

	router.GET("/home", func(c *gin.Context) {
		checkSession(c)
		c.HTML(http.StatusOK, "index.html", gin.H{})
	})
	routes.AuthRoutes(router)
	routes.UserRoutes(router)

	router.Run(":" + port)
}
