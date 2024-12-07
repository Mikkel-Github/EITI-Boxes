<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('reports', function (Blueprint $table) {
            $table->id();
            $table->string('company_name');
            $table->string('robot_model');
            $table->string('map');
            $table->string('route');
            $table->integer('orientations_tried')->default(0);
            $table->integer('runs')->default(0);
            $table->float('confidence')->check('confidence >= 0 AND confidence <= 1')->default(0);
            $table->integer('time_spent')->default(0);
            $table->integer('predicted_route_time')->default(0);
            $table->integer('boxes_moved_per_run')->default(0);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('reports');
    }
};
