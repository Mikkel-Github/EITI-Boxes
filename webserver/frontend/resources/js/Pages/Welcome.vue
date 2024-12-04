<template>
    <div class="" style="width: 100vw; height: 100vh;">
        <div class="Column" style="background-color: #212121; border-bottom: 2px solid #e9b66f;">
            <img src="../../images/logo.png" style="max-width: 6rem; height: auto;" />
        </div>
        <div class="Column H-Center">
            <h1 style="font-size: 48pt; text-align: center;">Welcome</h1>
            <h2 v-if="registering" style="font-size: 32pt; text-align: center;">Register</h2>
            <h2 v-else style="font-size: 32pt; text-align: center;">Log in</h2>
            <div class="Column H-Center Flex">
                <div class="Column V-Center Flex">
                    <transition name="slide-fade">
                        <input v-model="form.companyName.value" v-if="registering" placeholder="Company name" type="text" :class="{'InvalidInputField': !form.companyName.valid}">
                    </transition>
                        <input v-model="form.email.value" placeholder="Email" type="text" :class="{'InvalidInputField': !form.email.valid}">
                        <input v-model="form.password.value" placeholder="Password" type="password" :class="{'InvalidInputField': !form.password.valid}">
                    <transition name="slide-fade">
                        <input v-model="form.repeated_password.value" v-if="registering" placeholder="Repeat password" type="password" :class="{'InvalidInputField': !form.repeated_password.valid}">
                    </transition>
                    <button @mousedown="RegisterAccount" v-if="registering" class="btn btn-primary">Register</button>
                    <button @mousedown="LogIn" v-else class="btn btn-primary">Log in</button>
                </div>
                <hr style="width: 50%;">
                <p style="margin-bottom: 1rem;">or</p>
                <div class="Column H-Center" style="position: relative; min-width: 100%;">
                    <transition name="fade">
                        <button v-if="registering" @mousedown="registering = false" class="btn btn-primary" style="position: absolute;">Log in</button>
                        <button v-else @mousedown="registering = true" class="btn btn-primary" style="position: absolute;">Register</button>
                    </transition>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all .4s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-leave-active {
  transition: all .4s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-enter-from {
  transform: translateX(10px);
  opacity: 0;
}
.slide-fade-enter-to {
  transform: translateX(0px);
  opacity: 1;
}
.slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}
</style>

<script lang="ts">
import mqttService from '@/services/MqttService';

export default {
    data() {
        return {
            registering: true,
            form: {
                companyName: {value: "", valid: true},
                email: {value: "", valid: true},
                password: {value: "", valid: true},
                repeated_password: {value: "", valid: true},
            },
        }
    },
    props: {
    },
    computed: {
    },
    methods: {
        VerifyRegistrationForm(): bool {
            // No empty fields
            if(this.form.companyName.value == "") {
                this.form.companyName.valid = false
                return false
            }
            this.form.companyName.valid = true

            if(this.form.email.value == "" || !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.form.email.value)) {
                this.form.email.valid = false
                return false
            }
            this.form.email.valid = true

            if(this.form.password.value == "") {
                this.form.password.valid = false
                return false
            }
            this.form.password.valid = true

            if(this.form.repeated_password.value == "" || this.form.repeated_password.value !== this.form.password.value) {
                this.form.repeated_password.valid = false
                return false
            }
            this.form.repeated_password.valid = true

            return true
        },
        RegisterAccount() {
            if(!this.VerifyRegistrationForm()) {
                console.log(`Not valid registration form`)
                return
            }
            console.log(`Registering account: ${this.form.companyName}, ${this.form.email}, ${this.form.password}, ${this.form.repeated_password}, `)
        },
        VerifyLoginForm(): bool {
            if(this.form.email == "" || this.form.password == "") return false
            return true
        },
        LogIn() {
            if(!this.VerifyLoginForm()) {
                console.log(`Not valid login form`)
                return
            }
            console.log(`Logging in account: ${this.form.email}, ${this.form.password}`)
        }
    },
    mounted() {
    },
    beforeUnmount() {
    }
}
</script>
