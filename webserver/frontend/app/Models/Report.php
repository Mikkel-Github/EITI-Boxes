<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Report extends Model
{
    use HasFactory;

    protected $fillable = [
        'company_name',
        'robot_model',
        'map',
        'route',
        'orientations_tried',
        'runs',
        'confidence',
        'time_spent',
        'predicted_route_time',
        'boxes_moved_per_run',
    ];
}
