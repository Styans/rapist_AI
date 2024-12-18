package cookies

import "net/http"


const cookieName = "UUID"


func SetCookie(w http.ResponseWriter, val string, maxage int) {
	c := &http.Cookie{
		Name:     cookieName,
		Value:    val,
		MaxAge:   maxage,
		HttpOnly: true,
		Path:     "/",
	}
	http.SetCookie(w, c)
}


func GetCookie(r *http.Request) (*http.Cookie, error) {
	cookie, err := r.Cookie(cookieName)
	if err != nil {
		return nil, err
	}
	return cookie, nil
}

func DeleteCookie(w http.ResponseWriter) {
	cookie := &http.Cookie{
		Name:     cookieName,
		Value:    "",
		HttpOnly: true,
		Path:     "/",
		MaxAge:   -1,
	}
	http.SetCookie(w, cookie)
}