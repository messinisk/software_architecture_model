
# MVC vs MVVM — Αρχιτεκτονική Ιεράρχηση Συστήματος

Η τεκμηρίωση αυτή παρουσιάζει συνοπτικά τις δύο πιο διαδεδομένες αρχιτεκτονικές UI/logic separation: **MVC (Model–View–Controller)** και **MVVM (Model–View–ViewModel)**. Περιγράφει τη δομή τους, τη ροή δεδομένων και τις βασικές διαφορές τους, ώστε να αποτελέσει σημείο αναφοράς για επιλογή αρχιτεκτονικής σε web ή application projects.

---

## 🎯 Σκοπός
Να δοθεί μια καθαρή, πρακτική και συγκρίσιμη εικόνα των δύο patterns, με έμφαση στη **ιεραρχία**, τη **ροή δεδομένων** και τη **λογική παρουσίασης**.

---

## 🧩 MVC (Model–View–Controller)

### Δομή
- **Model** — Δεδομένα, ORM, business rules  
- **View** — UI templates (HTML, components, rendering layer)  
- **Controller** — Request handling, orchestration, σύνδεση Model → View  

### Ροή Δεδομένων
```
Request → Controller → Model → Controller → View → Response
```

### Χαρακτηριστικά
- Η λογική παρουσίασης βρίσκεται στον **Controller**.  
- Το View είναι **παθητικό** (δεν ενημερώνεται μόνο του).  
- Κατάλληλο για **server-side rendering**, REST APIs, κλασικά web frameworks.

---

## 🧩 MVVM (Model–View–ViewModel)

### Δομή
- **Model** — Δεδομένα και domain rules  
- **View** — UI components (reactive)  
- **ViewModel** — State, commands, business logic για το UI  

### Ροή Δεδομένων
```
View ↔ ViewModel → Model
```

### Χαρακτηριστικά
- Η λογική παρουσίασης βρίσκεται στο **ViewModel**.  
- Το View ενημερώνεται **αυτόματα** μέσω data-binding (one-way ή two-way).  
- Κατάλληλο για **SPA frameworks**, reactive UI, mobile/desktop apps.

---

## 🔍 Κύριες Διαφορές

| Τομέας | MVC | MVVM |
|-------|-----|------|
| Λογική παρουσίασης | Controller | ViewModel |
| Ενημέρωση UI | Χειροκίνητη | Αυτόματη (binding) |
| Σχέση UI ↔ Logic | Άμεση | Αποσυνδεδεμένη |
| Κατάλληλο για | Server-side apps | Reactive client-side apps |
| Διαχείριση state | Περιορισμένη | Πλούσια, κεντρική |

---

## 🧠 Πρακτικό Παράδειγμα

### MVC (Express)
```js
app.get('/users', async (req, res) => {
  const users = await User.find();
  res.render('users', { users });
});
```

### MVVM (Vue)
```js
export default {
  data() {
    return { users: [] };
  },
  async mounted() {
    this.users = await api.getUsers();
  }
};
```

---

## 📌 Συμπέρασμα
- Το **MVC** οργανώνει τη ροή γύρω από τον Controller.  
- Το **MVVM** οργανώνει τη ροή γύρω από το ViewModel και το reactive UI.  
- Η επιλογή εξαρτάται από το αν το UI είναι **server-driven** ή **client-reactive**.

